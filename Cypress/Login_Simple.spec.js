//Step 1: Login
describe('My First Test', () => {
  it('Visits the Kitchen Sink', () => {
    cy.visit('https://www.teammodel.net')
	cy.get(':nth-child(2) > .login-box-cont > .main > .subtitle').click()
	cy.get('#tmdID').type('guest')
	cy.get('#tmdpw').type('guest')
	cy.get('.iconFrame').click()
  })
})
