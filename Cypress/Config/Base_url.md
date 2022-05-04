```
打開你的配置文件 （cypress.json默認在你的項目目錄中）它開始是空的：

{}
讓我們添加baseUrl選項。

{
  "baseUrl": "http://localhost:8080"
}
這將自動使用此 baseUrl 作為前綴 cy.visit()和 命令。cy.request()

每當您修改配置文件時，Cypress 都會自動重啟並終止所有打開的瀏覽器。這很正常。再次單擊規範文件以重新啟動瀏覽器。

我們現在可以訪問相對路徑並省略主機名和端口。

describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('/')
  })
})
應該會 Pass 
```
