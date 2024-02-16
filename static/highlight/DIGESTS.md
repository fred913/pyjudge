## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
  integrity="sha384-xBsHBR6BS/LSlO3cOyY2D/4KkmaHjlNn3NnXUMFFc14HLZD7vwVgS3+6U/WkHAra"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"
  integrity="sha384-WmGkHEmwSI19EhTfO1nrSk3RziUQKRWg3vO0Ur3VYZjWvJRdRnX4/scQg+S2w1fI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-Qbgrf1REEH3h83e6HRrq1xAI7m7OMypPrpW6TLy6HiiPHu8CtlsqRpXdt6FOxdbb /es/languages/arduino.js
sha384-l1VXXq344qaos4PmR6Yteczej4EdX2RQZQZWWZAoLb2BcnWzJVpmAWd5AHj1UFeF /es/languages/arduino.min.js
sha384-tLSPlVe/SCeSVrXrvBRq+Ar+FGqR+H+kVy5YFSWtzyKfExg5NLG2vwg207tTKyHQ /es/languages/armasm.js
sha384-pJoNPslHHsgF8oWC+6BTz8z51WuwRvC9FZDIthPkCWH08v+5qV99ZM5rSaiTqEHl /es/languages/armasm.min.js
sha384-uBlc/xEFeDxZmBU7K/YWwi3ryXQrLQCAY2K1Dl3OD2DaAQBZZTt6Ew3aeDP20ix0 /es/languages/bash.js
sha384-4qer4rJCVxZjkwD4YaJfOnT2NOOt0qdjKYJM2076C+djiJ4lgrP1LVsB/MCpJSET /es/languages/bash.min.js
sha384-EwAFcMMnNYbOS/ABVtPlSLENfB27fQSxa/eUw9xWLejr7sWWPcICSoHJUxNVwhgI /es/languages/basic.js
sha384-3EDvjyClCK85gMCNUIHh/H9+K30vwYJjkGmjdUKpG6bGxahP+dSc+HRtXadT8eUD /es/languages/basic.min.js
sha384-0OZaeLK1yb5eP3nW4y0JP1fVharSrsuv/1mkI/6/8aRFm9laYIWIMXjCOqu+vRW5 /es/languages/c.js
sha384-G7WtwjMBNGrPly3ZsbPhfnT0v88hG3Ea9fQhrSWfzj7cNAsXsU7EKMQLyLGj7vTH /es/languages/c.min.js
sha384-69o7b7hP4COEFD4DUeWD/evW62WGzW4jk3uIuQ5l8Ogi2TM2ICVVaUYO8DTmIktm /es/languages/coffeescript.js
sha384-hs3Egk+9CzC2kK7ZZLBVUrgiyFcI/OzhECFhJzoD2Qm2ipxDbrwCTQAh/RTkuo6c /es/languages/coffeescript.min.js
sha384-Wjwd1YEG/PYlkLHTWIx+RlPK6XboMN3bEpveERJ8D8Z4RaNE02Ho19ZFrSRPGi0j /es/languages/cpp.js
sha384-Q4zTNH8WsDVdSZbiZtzWS1HmAUcvMSdTmth9Uqgfjmx7Qzw6B8E3lC9ieUbE/9u4 /es/languages/cpp.min.js
sha384-DA5ii4oN8R2fsamNkHOanSjuN4v7j5RIuheQqnxMQ4cFnfekeuhwu4IdNXiCf+UU /es/languages/css.js
sha384-OBugjfIr093hFCxTRdVfKH8Oe3yiBrS58bhyYYTUQJVobk6SUEjD7pnV8BPwsr8a /es/languages/css.min.js
sha384-nJZn4t0S58K5MJ/2BOmgkTC8TtBWB76ykEKIIzb8sUxT3h7ouZH5Ucqnr9MJ6Bry /es/languages/diff.js
sha384-OIJrZgyhN1E6e29B9M3gFPtkR5JgXpls8h5D2bNzBxQ8Ncwxzfjedu3/0jZEe7S9 /es/languages/diff.min.js
sha384-7m427rj9OYl8KKObOk+aD0QhXmqXy6hU/sHGS6OUwW9hRiiHvr+tLTbLiSJYbIyD /es/languages/http.js
sha384-GdKwMgTrO0R3SPXhm+DuaN3Qr7WkqYmmTClINAGPuV/BUPE9WUI/WnTEntp522Sl /es/languages/http.min.js
sha384-7hMYwsnoFLW0Wnjv4vRnZxuedW1tCz7/pydl1b9w3fg7B+rldToCjqzXwCRHUE7C /es/languages/ini.js
sha384-LDu6uT3diI3jBUJtdoGFa787cYlVrR+aqFfmW+kW+TImOkpVe+P5LBdDzydIHo9Z /es/languages/ini.min.js
sha384-WFJdA9Hz+G9NQx5vPba/tcGyIibm57UkKVY32wNB/94iT2FmPma5W7gY8p2l6qps /es/languages/java.js
sha384-coaxfgI2lKuDqSxfMlfyPq5WM0THaLGyATZHzaFMrWdIbPcLdduuItTe6AmT/m33 /es/languages/java.min.js
sha384-WCznKe2n87QvV/L1MlXN+S8R6NPUQGU34+AqogMuWGZJswSD6rt3Mgih+xuKlDgm /es/languages/javascript.js
sha384-eGsBtetyKPDKaLiTnxTzhSzTFM6A/yjHBQIj4rAMVaLPKW5tJb8U6XLr/AikCPd+ /es/languages/javascript.min.js
sha384-12GbYFzdyZCSmfBTmO2CR/qE89K5uE1PEuJ3QUwXH0Q9u+uoLNigjH9dG7LAxxiI /es/languages/json.js
sha384-+DT7AtubDhVDciRc6CgjJJRsCt0L8NC3Dh8n9Tj2tZWU8rWxDIj1ViubmUDn8OCY /es/languages/json.min.js
sha384-iBzB3Gn/ezqfaxd3xkqjVlWlUdqCAcOUBIjD5IQGs9p7tbFNU8ymlgKpDsGRGaDQ /es/languages/less.js
sha384-04z6U6c1rUG3NEMdXE8dOimK4VJx8yGR1D5qKHgS7319t9s27xfmtQLQKC6jDUuY /es/languages/less.min.js
sha384-bWwkdmOCj83zZ8/m+oPD9goRMhrPCb25ZA6aTyg7vcsq9IpuyED38kQSw1Na4UTZ /es/languages/markdown.js
sha384-SqGSUq0DMQ0OUQnQnTuVDCJyhANd/MFNj+0PF67S+VXgHpR8A4tPsf/3GoSFRmrx /es/languages/markdown.min.js
sha384-eYjnCHZ0BK3k5isHatk8c3+BaQEksfwQwPL1t6JhdY+mqPXinr7GS8Oo/1ge4yLo /es/languages/mipsasm.js
sha384-0Qx9PV0NMTFk+RqaKeTcoj6XqYesVvfXoezvsEiXyFqeO17iMKoo0vvQ9rRFNRoc /es/languages/mipsasm.min.js
sha384-TTDGPCrk8Dg2oW6NghGM5WJQPbi34BdYJj6yfsDiGXlM5os/SebXT6KzATp19rzo /es/languages/plaintext.js
sha384-XXx7wj9KPm08AyGoGzzFKZP2S7S+S5MbKMPnQcWUyhJ3EjHvLuctK/O1ioJnG2ef /es/languages/plaintext.min.js
sha384-+5oyk7Ed3OlvEWGj8xracq/6e52BScKUN4kxcreNwB7kfRTVsAMs/aAJM58dzIFN /es/languages/python.js
sha384-ND/UH2UkaeWiej5v/oJspfKDz9BGUaVpoDcz4cof0jaiv/mCigjvy7RQ7e+3S6bg /es/languages/python.min.js
sha384-BSeMSSkpHXATzXVnQDrjF2DPTOBSrKP8QqV0DcEVYa5k6JK9CSYxFKyEhj+Kqnde /es/languages/python-repl.js
sha384-sW9zIYfNc+qN/lya5oAmIdFlVbXjPLcdYkPSdRMpxO/xI2jbDW/Q4Etvx02DFOmf /es/languages/python-repl.min.js
sha384-lRhSX2XDrY27NzrAS1t4YaeRtwjsY41kFBbIEYltkmnsfSE7lbBJMQVds2u/MqTT /es/languages/scss.js
sha384-RDUehV4j9Do6iGkYq9Gjn3aUxh6x+NFER1sHpLUXsNoCFjah8Ysrlad8ukLbIr4J /es/languages/scss.min.js
sha384-2o3vNanj3riyfakWVTrzuX2nYW2UuBkJj1rquQdK97wNLsUMW/YtTGBx/y6YrZ8d /es/languages/smali.js
sha384-u0+HbQcahC6m0dedTQHD/+4ltin4W9rjZQxNGBEW/6/ORehGOvu1LXEkhWWrLb3W /es/languages/smali.min.js
sha384-C5Ib6vLvFc6BpxyyN5165sVTrN05Avl4ADMSVNVSmB61oPr42vOavsZlxOknqqWz /es/languages/wasm.js
sha384-FlAOV+6BVjUyajzW4twmqUvHxDYallf5jw5FewMZmsBHBuiJ/CJj1NZhNT1fHuzT /es/languages/wasm.min.js
sha384-RO3jZ153V5Jqty8zR67qviMBlAYXKZ2mCFqEdCUlPJFKVRgkUVpeuXbvM8mGZqGl /es/languages/x86asm.js
sha384-POvW54o3Z6xZV0L2TM4VgkaKxfrnDTCf3nfOeA+Szz73C2dm7jL8CRGlBtM0FHMr /es/languages/x86asm.min.js
sha384-OFoR8IZ+CFwcY8plx8HSDZNoCwLxc701CwdNGfoIEhSgwAbwhvInaxnEi3HYTt2Q /es/languages/xml.js
sha384-yFd3InBtG6WtAVgIl6iIdFKis8HmMC7GbbronB4lHJq3OLef3U8K9puak6MuVZqx /es/languages/xml.min.js
sha384-cZ/PFW75r8K/XQ1B9mwtLIR8nqjfV9wgjYdpBn5XCh8ev/XEJypupev/bfOSmdNP /languages/arduino.js
sha384-FWCBHZ/wFcOZ5LXWHV3JINd24NzsjJtrIkqaIlpVJpJcjng5ALM8AA/qumGEZQ4W /languages/arduino.min.js
sha384-hM6AXFyXHWRaXr4eiXrkJY8/TBXao0j5MTAXVULUHAUmocFzxPTLeekpDkCuvpcN /languages/armasm.js
sha384-60YzKSwA14gAvQbuEe+XjCv2EepzDhDjELBciyGY30m9yD6zdxPDVakewhURpuJY /languages/armasm.min.js
sha384-qbbaBGYYg7PdopdWOGj8KdkBosUDY5PAe3aTMJKTqWcriPBJJzCVu5BlwNEwqr9U /languages/bash.js
sha384-ByZsYVIHcE8sB12cYY+NUpM80NAWHoBs5SL8VVocIvqVLdXf1hmXNSBn/H9leT4c /languages/bash.min.js
sha384-KNVj6C9bNyJrl0feAi64iBCZkXxoTQxDbAJqGlVos5lGlSTOHd+zE1xQgkPFoH4t /languages/basic.js
sha384-KfOKKkbUp6gWmUdMPNCj5Hqqmf9Z03BTs0GnM3hyrYlNBYXSt4O527wBkKrgxiIl /languages/basic.min.js
sha384-VZxKf0mjKYDwZIgrW+InqDfJ0YwYUFEMw/4YmpV1oKtVXFVmVq/Ga1vgq6zKTUqS /languages/c.js
sha384-mWenE7UXKnmYRcJ3mh+Os3iZ43BmFf9x3AZMM6gi/2sT6vxouPWspbTdREwWDO3w /languages/c.min.js
sha384-WUNn1g8nanfA0JIzB9I7thYK5lEx4KCzTXft6eLUiSXrFT8gHOk4MU9CHr/J4EB4 /languages/coffeescript.js
sha384-LAzSkWYZ3FWRTDwn+LHzyO1jGUFT5FYSAABzOTE4lsm429sEXm0+U7A5i73hhMSz /languages/coffeescript.min.js
sha384-J4Ge+xXjXgzbK2FP+OyzIGHLfKU/RR0+cH4JJCaczeLETtVIvJdvqfikWlDuQ66e /languages/cpp.js
sha384-LMyrRAiUz6we2SGvYrwDd4TJoJZ+m/5c+4n4E64KVkfWFcZdlrs4Wabr0crMesyy /languages/cpp.min.js
sha384-r9czyL17/ovexTOK33dRiTbHrtaMDzpUXW4iRpetdu1OhhckHXiFzpgZyni2t1PM /languages/css.js
sha384-HpHXnyEqHVbcY+nua3h7/ajfIrakWJxA3fmIZ9X9kbY45N6V+DPfMtfnLBeYEdCx /languages/css.min.js
sha384-d6WNn2kPYgdezhgRmGehSkGVKwbg+ImJrGTA43yYg8VsBqYW5TakSDi/jbVjzqfD /languages/diff.js
sha384-yE0kUv4eZRBzwnxh0XmeqImGvOLywSpOZq2m0IH40+vBtkjS716NYEZyoacZVEra /languages/diff.min.js
sha384-g/lhU6FXH73RQL4eFwkPk4CuudGpbHg6cyVZCRpXft3EKCrcQTToBVEDRStjYWQb /languages/http.js
sha384-wt2eEhJoUmjz8wmTq0k9WvI19Pumi9/h7B87i0wc7QMYwnCJ0dcuyfcYo/ui1M6t /languages/http.min.js
sha384-JSUMPR+WT0h/7NlqXi1Al9bVlNT31AeZNpAHttuzu+r02AmxePeqvsZkKqYZf06n /languages/ini.js
sha384-QrHbXsWtJOiJjnLPKgutUfoIrj34yz0+JKPw4CFIDImvaTDQ/wxYyEz/zB3639vM /languages/ini.min.js
sha384-pYIeBYeCE96U9EkPcT4uJjNWyrB1BKB41JIadYJbvmGa5KacaoXtSQOUpBfeyWQX /languages/java.js
sha384-uUg+ux8epe42611RSvEkMX2gvEkMdw+l6xG5Z/aQriABp38RLyF9MjDZtlTlMuQY /languages/java.min.js
sha384-vJxw3XlwaqOQr8IlRPVIBO6DMML5W978fR21/GRI5PAF7yYi2WstLYNG1lXk6j9u /languages/javascript.js
sha384-44q2s9jxk8W5N9gAB0yn7UYLi9E2oVw8eHyaTZLkDS3WuZM/AttkAiVj6JoZuGS4 /languages/javascript.min.js
sha384-dq9sY7BcOdU/6YaN+YmFuWFG8MY2WYJG2w3RlDRfaVvjdHchE07Ss7ILfcZ56nUM /languages/json.js
sha384-RbRhXcXx5VHUdUaC5R0oV+XBXA5GhkaVCUzK8xN19K3FmtWSHyGVgulK92XnhBsI /languages/json.min.js
sha384-1c9TXIjKaFE96Q8dzV+3AF30su8LWfRZ6/PIqg1gPNQo+LMeGHwB602qIjQQ+CgC /languages/less.js
sha384-nT7qGhTl7ILVe2/0D834KL+fN+VL4uJg7GFmHHF8YMIg3LSbOrihvebWz6A6KLMD /languages/less.min.js
sha384-U+zIQPoVdPCO0o4poik2hYNbHtNm+L5OojDTulgIeEZTNz+LooLAm72d66mNjwKD /languages/markdown.js
sha384-mCUujHHbWJEjcupTTfWOk9YR3YCYNHaA578+TTXUd4LPi7fGNuMQbysbl1pmcIGd /languages/markdown.min.js
sha384-IYme+6MmtND/HdSTw8zZry0hiC+EVwHHRuTJDu7M1DZcd6SAbZSGJ+pBgafCszHL /languages/mipsasm.js
sha384-JuwM4QgALf4/n2PaHzRCU3ppICcAenDKOyhbrthq99UkLQOkEVdSf0Eig9g64vNI /languages/mipsasm.min.js
sha384-IHapUcPkNR+7JNsR+qYSVYGCE3Dpzo2//VYWtmGYrw3eQG1RItQ7HYq6aK1Jo/6L /languages/plaintext.js
sha384-ofjxHpechXkaeQipogSyH62tQNaqAwQiuUHOVi4BGFsX5/KectIoxz16f8J/P5U0 /languages/plaintext.min.js
sha384-zdZio5RcGiKQJCpe/1IXujPle3bIY8sbmvCabSU5G5GzWAzZtoRZfg9QAQXCL08q /languages/python.js
sha384-IP4vv4Aoh9Lyg8QyzVkAmn2JGoDCpgVHzVSrD3Z+rVyn7+s4wx4pRjv+go3TEwfj /languages/python.min.js
sha384-7jEUoPRiHUgJOTai1kMkoxn2EnF86LMvN/MagHBb2SlmmV6Xd4jlrgQfLTzgM3sP /languages/python-repl.js
sha384-bKSBGjy2/8jltjSAlvCjAvEvjy8osMZfj37sBThcXS7n6SppraMRghmLmAxiapyN /languages/python-repl.min.js
sha384-fwYddFsITuK2bPhi9RuIzwi4PTULEXgtEJsQzTdx97vOS/GHfrk+aNSLxEHgzQa5 /languages/scss.js
sha384-6u+QpCDqQidb5pcO+yBqy0xLJ30x30VlrFvXm8J84LMwGIw9q3U4u+Z9vFXlhB5x /languages/scss.min.js
sha384-7hSFTOdydm8A24wK+QK9VTkrCg10EysXSbATY3j20MhphArrePJ7OTGqgz498CrI /languages/smali.js
sha384-0szVjKKATgtBXpYE6ZwLFEaR+msbyW5uBxx4hqaWpPJ0A+yf1P8czY+QxYF9prTH /languages/smali.min.js
sha384-ry6bgnkpMB819ITiAptb7x+iphp9TkAJTFl2NZQfF7JCOxZE+DcJvsAUvP2t4Ccn /languages/wasm.js
sha384-fWMR10q8HCFcv4u/2S/P5JHw477fD1akWW/mGsZNig4vAOk4135GEWJft9llui8U /languages/wasm.min.js
sha384-VTxXvfgFdouwB5elGbSe4HkcLE8fIIWv/8Zed/4/Fynu8i3w3DPVPJLO3qGGsZXB /languages/x86asm.js
sha384-eKsHYF6apOh4wN/zUOnYUx5s4086rCTH2ZG0R09R49HLu6/1Kn/6J7Zn6M8++8On /languages/x86asm.min.js
sha384-+PuZYFfVX2UQZU2yKt/FsJUZNUPzZWxW7auXltsaecr1xLvzBYF3c5gYoyOs1++x /languages/xml.js
sha384-jgkY4GMNWfQcLLIoP1vg3FWXflDrRhcSXGBW6ONIWC2SOIv5H1Pa57sXs+aomCuZ /languages/xml.min.js
sha384-HWPaWe6WO6of94LoQ42XRMVJe4dpTAR2seomXFPmFKMNgfczfrW5jzb4WNwS5AyU /highlight.js
sha384-mDxkKIK42ubVOVon2VI2U4BvLqg8mb6zPv2BBZdS+jStRy16HDyRvE+YtQHEDLLD /highlight.min.js
```

