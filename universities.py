import re;
import bs4;
import requests;
from bs4 import BeautifulSoup;

def getHTMLText(URL):
    try:
        r= requests.get(URL, timeout=30);
        r.raise_for_status();
        r.encoding = r.apparent_encoding;
        return r.text;
    except:
        return "An exception occured :(";

def fillUniList(uniList, html):
    soup = BeautifulSoup(html, "html.parser");
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all("td");
            uniList.append([tds[0].string, tds[1].
                            string, tds[2].string, tds[3].string]);
            

def printUniList(uniList, num):
    print("{:^15}\t{:^15}\t{:^30}\t{:^15}"
          .format("Rank","University","City","Score"));
    for i in range(num):
        u = uniList[i];
        print("{:^15}\t{:^15}\t{:^15}\t{:^15}"
              .format(u[0],u[1],u[2],u[3]));
        
def main():
    uniInfo = [];
    URL = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html";
    html = getHTMLText(URL);
    fillUniList(uniInfo, html);
    printUniList(uniInfo, 100);

main();


