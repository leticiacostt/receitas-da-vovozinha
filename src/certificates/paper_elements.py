class A4Object(object):
    width = 297.0
    height = 210.0
    centerx = width / 2
    centery = height / 2
    margin_left = 20
    margin_top = 20
    margin_right = width - margin_left
    margin_bottom = height - margin_top

A4 = A4Object()

class Rectangule(object):
    left = A4.centerx
    top = A4.centery
    width = 50.0
    height = 50.0
    bottom = top+height
    right = left+width
    def update(self):
        self.bottom = self.top+self.height
        self.right = self.left+self.width

Logo = Rectangule()
Logo.left = A4.centerx-10
Logo.top = 10.0
Logo.width = 20.0
Logo.height = 10
Logo.update()

Footer = Rectangule()
Footer.left = 0.0
Footer.top = A4.height-25
Footer.width = A4.width
Footer.height = 25
Footer.update()