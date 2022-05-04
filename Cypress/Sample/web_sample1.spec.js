// Strat Cypress 
// npx cypress open

//Step 1: Login 
describe('入校老師新建個人班級', () => {
  it('Login', () => {
    cy.visit('https://www.teammodel.net')
	cy.get(':nth-child(2) > .login-box-cont > .main > .subtitle').click()
	cy.get('#tmdID').type('guest')
	cy.get('#tmdpw').type('xxxx')
	cy.get('.iconFrame').click()
	cy.wait(1000)
  })
  
  it('Visits 學生管理', () => {
    cy.visit('https://www.teammodel.net/home/studentAccount/StuMgt')
  	cy.get(':nth-child(2) > .login-box-cont > .main > .subtitle').click()
  })
})
