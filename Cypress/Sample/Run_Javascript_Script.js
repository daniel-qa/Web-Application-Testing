// Demo.spec.js created with Cypress
//
// Start writing your Cypress tests below!
// If you're unfamiliar with how Cypress works,
// check out the link below and learn how to write your first test:
// https://on.cypress.io/writing-first-test

//Step 1: Login 
describe('Run Javascript Script', () => {
	it('改變 Google 字串內容', () => {
	
		cy.visit('https://www.google.com/');
		cy.window().then((win) => { 
			win.document.getElementsByName('btnK')[1].value = "Ganesh" 
		});
	})
	
	// document.getElementById("login").style.display = "none"; //（login为需要隐藏的页面ID）

	// document.getElementById("regist").style.display = "block"; //（regist为需要显示的页面ID）

})
