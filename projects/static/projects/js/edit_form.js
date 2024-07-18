window.addEventListener("DOMContentLoaded", function() {
    alert = document.createElement("div")
    h1 = document.getElementsByTagName("h1")
    if (h1.length) {
        alert.innerHTML = h1[0].innerHTML
        alert.style.margin = "0.5% 2%"
        alert.classList = "alert alert-success"
        document.getElementsByTagName("h1")[0].outerHTML = alert.outerHTML
    }       
    
    form = document.getElementsByClassName("form-control")[0]
    elements = form.children
    
    description = elements[1]
    description.innerHTML = (description.children)[0].outerHTML + document.createElement("br").outerHTML + (description.children)[1].outerHTML

    contents = elements[5]
    contents.innerHTML = (contents.children)[0].outerHTML + document.createElement("br").outerHTML + (contents.children)[1].outerHTML
    contents.children[2].style.marginLeft = "15%"
    // content_div = contents.children[1]
    // content_div.innerHTML = content_div.children[0].outerHTML + content_div.children[2].outerHTML

    text_areas = form.getElementsByTagName("textarea")
    for (let index = 0; index < text_areas.length; index++) {
        const element = text_areas[index];
        element.style.width = "100%"
    }

    for (let index = 0; index < elements.length; index++) {
        const element = elements[index];
        element.style.margin = "2% 0"
        element.style.width = "90%"
        
        if(index != 5 && index != 6) {
            element.children[1].style.width = "75%"
        }
    }
}, false);