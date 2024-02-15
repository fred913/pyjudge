window.$ = mdui.$

$.extend({
    get: (url, callback, fail) => {
        $.ajax({ method: "GET", url: url }).then(callback).catch(fail)
    }, post: (url, payload, callback, fail) => {
        $.ajax({ method: "POST", url: url, data: payload }).then(callback).catch(fail)
    },
})