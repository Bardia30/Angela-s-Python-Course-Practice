#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from turtle import Turtle, Screen


# In[ ]:


timmy = Turtle() #Turtle is a class (it starts with capital case)


# In[ ]:


print(timmy)
timmy.shape("turtle")
timmy.color("coral")


# In[ ]:


#car.speed (object.attribute)
#car.stop() (object.method())


# In[ ]:


my_screen = Screen()
print(my_screen.canvheight)
timmy.forward(100)
my_screen.exitonclick()


# In[9]:


import prettytable
from prettytable import PrettyTable
table = PrettyTable()


# In[10]:


table.field_names = ["City","Population"]
table.add_row(["Tehran",80000000])


# In[6]:


print(table)


# In[15]:


table.del_column("Area")
print(table)


# In[18]:


pokemon = PrettyTable()


# In[19]:


pokemon.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
pokemon.add_column("Type",["Electric","Water","Fire"])


# In[21]:


pokemon.align = "l"
print(pokemon)


# In[30]:


#Coffee Machine in OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# In[31]:


menu.get_items()


# In[41]:


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# In[40]:


coffee_maker.report()
money_machine.report()


# In[37]:


coffee_maker.is_resource_sufficient()


# In[48]:


is_on = True
while is_on:
    options = menu.get_items()
    choice=input(f"What would you like?{options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            


# In[ ]:




