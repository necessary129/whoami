import jinja2
import pathlib
from yaml import load, Loader
import markdown
import requests
import gnupg
from datetime import datetime,timezone

identities = pathlib.Path("identities")

with (identities / "conf.yaml").open() as f:
    conf = load(f, Loader=Loader)


def getsign(message):
    gpg = gnupg.GPG()
    sign = gpg.sign(message)
    return sign.data


def genmisc():
    miscpath = identities / "misc"
    misc = []
    for mdir in miscpath.iterdir():
        with (mdir / "content.md").open() as f:
            content = markdown.markdown(
                f.read().strip(), extensions=["markdown.extensions.extra"]
            )
        with (mdir / "title").open() as f:
            title = f.read().strip()
        misc.append({"content": content, "title": title})
    return misc


def getbtcblock():
    btcdata = requests.get("https://blockchain.info/latestblock").json()
    return {
        "hash": btcdata["hash"],
        "height": btcdata["height"],
        "url": "https://www.blockchain.com/btc/block/{}".format(btcdata["hash"]),
    }


def placeurl():
    with (identities / "url").open("w") as f:
        f.write(conf['url'])


def gentemplate():
    with open("index.html.j2") as f:
        template = f.read()
    jtemplate = jinja2.Template(template)
    return jtemplate.render(
        conf=conf, btchash=getbtcblock(), misc=genmisc(), date=datetime.now(timezone.utc).strftime("%X %x %Z")
    )


def main():
    html = gentemplate()
    html = "-->\n{}\n<!--".format(html).encode("utf8")
    signed_html = getsign(html).decode("utf8")
    out_html = "<!--\n{}\n-->".format(signed_html)
    with open("out/index.html", "w") as f:
        f.write(out_html)
    placeurl()


if __name__ == "__main__":
    main()
