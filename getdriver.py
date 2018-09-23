import argparse
import sys
import urllib.request as request
from io import BytesIO
from zipfile import ZipFile


MIRROR = "https://chromedriver.storage.googleapis.com"
LATEST = "LATEST_RELEASE"


class GetDriver:
    def __init__(self):
        self.mapping = {
            "darwin": self.darwin,
            "linux": self.linux,
            "win32": self.win32
        }

    def latest(self, dir=".", platform="linux"):
        find_version = self.version()
        zip_download = self.mapping[platform](find_version)
        zip_object = ZipFile(BytesIO(zip_download)).extractall(dir)
        result = {"version": find_version, "platform": platform,
                  "status": "success"}
        return result

    def version(self):
        url = "%s/%s" % (MIRROR, LATEST)
        req_object = request.urlopen(url)
        result = req_object.read().decode('utf-8')
        return result

    def linux(self, version):
        path = "chromedriver_linux64.zip"
        url = "%s/%s/%s" % (MIRROR, version, path)
        result = request.urlopen(url).read()
        return result

    def darwin(self, version):
        path = "chromedriver_mac64.zip"
        url = "%s/%s/%s" % (MIRROR, version, path)
        result = request.urlopen(url).read()
        return result

    def win32(self, version):
        path = "chromedriver_win32.zip"
        url = "%s/%s/%s" % (MIRROR, version, path)
        result = request.urlopen(url).read()
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, default=".", required=False,
                        help='Path where to extract chromedriver')
    parser.add_argument("-p", "--platform", type=str, required=False,
                        default=sys.platform,
                        help='Specify to download specific OS driver')
    args = parser.parse_args()
    print(GetDriver().latest(args.dir, args.platform))
