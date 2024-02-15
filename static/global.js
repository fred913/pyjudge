window.$ = mdui.$

$.extend({
    get: (url, callback, fail) => {
        $.ajax({ method: "GET", url: url }).then(callback).catch(fail)
    }, post: (url, payload, callback, fail) => {
        $.ajax({ method: "POST", url: url, data: payload }).then(callback).catch(fail)
    },

    highlightFromMarkdown: () => {
        // load code blocks
        $.each($("code"), (_, elem) => {
            // is multi-line code block?
            var codeString = $(elem).text()
            if (codeString.indexOf("\n") > 0) {
                var splitTokenIndex = codeString.indexOf("\n")
                var codeStringCode = codeString.substring(splitTokenIndex + 1)
                var langName = codeString.substring(0, splitTokenIndex)
                console.log(elem)

                var hl = hljs.highlight(codeStringCode, { language: langName })
                var cnt = document.createElement("pre")
                cnt.classList.add("descmd-code-block")
                cnt.innerHTML = hl.value.replace(/\n/g, "<br />")
                elem.outerHTML = cnt.outerHTML
            }
        })
    }
})