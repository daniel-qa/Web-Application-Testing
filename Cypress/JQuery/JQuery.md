```
You can also query DOM elements with cy.$$. But Cypress.$ and cy.$$ are different.

Cypress.$ refers to the jQuery function itself. You can do anything with Cypress.$ if you can do it with the jQuery function. 
```

# window
```
cy.visit('http://localhost:8080/app')
cy.window().then((win) => {
  // win is the remote window
})
```
# jQuery

```
$(this).hide() - hides the current element.

$("p").hide() - hides all <p> elements.

$(".test").hide() - hides all elements with class="test".

$("#test").hide() - hides the element with id="test".
```

```
Cypress.$('p')


$("p").hide()- 隱藏所有 <p> 元素。
  
  
  
$("#myimg").hide();
$("#myimg").show();



$(".w-e-up-img-container div").show;
```
