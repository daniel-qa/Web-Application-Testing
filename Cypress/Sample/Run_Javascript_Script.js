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

})
