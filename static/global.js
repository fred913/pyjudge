window.$ = mdui.$

$.extend({
    get: (url, callback, fail) => {
        $.ajax({ method: "GET", url: url }).then(callback).catch(fail)
    }, post: (url, payload, callback, fail) => {
        $.ajax({ method: "POST", url: url, data: payload }).then(callback).catch(fail)
    },

    highlightFromMarkdown: () => {
        // load code blocks
        $.each($("pre"), (_, elem) => {
            $.each(elem.querySelector("code").classList, (i, v) => {
                if (v.startsWith("language-")) {
                    var langName = v.substring(v.indexOf("-") + 1)
                    console.log(langName)

                    var codeString = $(elem).text()
                    console.log(elem)

                    var hl = hljs.highlight(codeString, { language: langName })
                    var cnt = document.createElement("pre")
                    cnt.classList.add("descmd-code-block")
                    cnt.innerHTML = hl.value
                    elem.outerHTML = cnt.outerHTML
                }
            })
        })

    }
})
