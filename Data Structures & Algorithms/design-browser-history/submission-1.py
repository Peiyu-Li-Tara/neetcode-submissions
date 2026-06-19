class BrowserHistory:

    def __init__(self, homepage: str):
        self.home_page = Page(homepage)
        self.dummy_end_page = Page("")
        self.curr_page = self.home_page

        self.home_page.next = self.dummy_end_page
        self.dummy_end_page.prev = self.home_page
        

    def visit(self, url: str) -> None:
        # print(self.curr_page.url)
        self.curr_page.next = self.dummy_end_page
        self.dummy_end_page.prev = self.curr_page
        
        new_page = Page(url)
        new_page_prev = self.dummy_end_page.prev
        new_page_next = self.dummy_end_page

        new_page_prev.next = new_page
        new_page_next.prev = new_page
        new_page.prev = new_page_prev
        new_page.next = new_page_next
        
        self.curr_page = new_page
        print("after visit: ", self.curr_page.url)
        

    def back(self, steps: int) -> str:
        print("start back, current page: ", self.curr_page.url)
        while self.curr_page and steps > 0:
            steps -= 1
            self.curr_page = self.curr_page.prev
            # print(self.curr_page.url)
        # print(steps, self.curr_page.url)
        
        if self.curr_page and steps == 0:
            return self.curr_page.url
        self.curr_page = self.home_page
        return self.curr_page.url
        

    def forward(self, steps: int) -> str:
        print("start forward current page: ", self.curr_page.url)
        while self.curr_page and steps > 0:
            steps -= 1
            self.curr_page = self.curr_page.next
        
        # print(steps, self.curr_page.url)
        if self.curr_page and self.curr_page != self.dummy_end_page and steps == 0:
            print("after forward: ", self.curr_page.url)
            return self.curr_page.url
        self.curr_page = self.dummy_end_page.prev
        print("hit end: ", self.curr_page.url)
        return self.curr_page.url


class Page:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)