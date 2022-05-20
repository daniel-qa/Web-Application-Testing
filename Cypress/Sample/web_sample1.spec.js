// Strat Cypress 
// npx cypress open

//Step 1: Login 
describe('入校老師新建個人班級', () => {
	beforeEach(() => {
		cy.visit('https://www.xxx')
		cy.get(':nth-child(2) > .login-box-cont > .main > .subtitle').click()
		cy.get('#tmdID').type('guest')
		cy.get('#tmdpw').type('0000')
		cy.get('.iconFrame').click()		
		cy.get('.lock-menu-btn')
  })
  
  it('查看個人資訊', () => {	  		
		cy.get('.avatar').click()
		cy.wait(1000)
		cy.contains('sidxxxxxx')
  })
	
  // Just For Demo	
  it('輸入字串', () => {	  		
		cy.get('.action-email')
		  .type('fake@email.com')
		  .should('have.value', 'fake@email.com')	
})

//  css=.exersices-content .w-e-text p
//  文字輸入框，直接定位(type)最後的儲存元素容器，比如 <p>123</p>	
