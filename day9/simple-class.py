class Duck:
    sound = 'Quaaack!'
    walking = 'Walking likes a duck'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

if __name__ == '__main__':
    donald = Duck()
    donald.quack()
    donald.walk()
