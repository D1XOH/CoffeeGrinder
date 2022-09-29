class CoffeeGrinder:
	beans = 0
	coffee = 0

	def put_beans(self, count_beans):   # Метод, используемый для того чтобы положить бобы в машину
		self.beans += int(count_beans)

	def grind(self):                    # Метод превращающий все бобы в молотый кофе 1 к 1
		if self.beans == 0:
			print('Нет бобов')
		else:
			self.coffee += self.beans
			print('Сделано молотого кофе:', self.beans)
			self.beans = 0  # После превращения бобов в молотый кофе, обнуляем кол-во бобов в гриндере


class FrenchPress:
	coffee_drink = 0  # Переменная для подсчёта напитков кофе
	water = 0  # Переменная для подсчёта воды
	coffee = CoffeeGrinder.coffee  # Если перемолоть бобы в молотый кофе, то молотый кофе будет использован в этом классе, иначе молотый кофе будет равен 0

	def put_water(self, water):  # Метод, используемый для того чтобы налить воды в автомат
		self.water += water

	def put_coffee(self, coffee): # Метод, используемый для того чтобы положить молотый кофе в автомат
		self.coffee += coffee

	def make_coffee_drink(self, count):  # Метод для приготовления напитка кофе
		coffee_drink_requirement = 1
		if self.coffee == 0 or self.water == 0:
			print(f'В машине отсутствует молотый кофе или вода ')
		else:

			if count > self.coffee or count > self.water:
				print(f'Невозможно сделать {count} кофе из-за нехватки ингридиентов в автомате.\n'
				  	f'Требуется {count} молотого кофе и {count} воды')
			else:
				self.coffee_drink += count  # Увеличиваем количество приготовленого кофе, имеющегося в автомате
				print('Сделано кофе', self.coffee_drink)
				self.coffee -= count  # Уменьшаем количество молотого кофе в автомате, после приготовления n количества кофе
				self.water -= count  # Уменьшаем количество молотого воды в автомате, после приготовления n количества кофе

	def get_coffee_drink(self, count):  # Метод, используемый для выдачи напитков кофе из автомата
		if self.coffee_drink == 0:
			print('Кофе нет')
		elif count > self.coffee_drink:
			print('Невозможно выдать кофе больше, чем есть в автомате:', self.coffee_drink)
		else:
			print('Выдано кофе', count)
			self.coffee_drink -= count  # Уменьшаем количество напитков кофе в автомате, после выдачи n количества кофе

	def count_coffee_drink(self):  # Метод для получения информации о количество напитков кофе, имеющегося в автомате
		print("Количество кофе хранящегося в автомате: ", self.coffee_drink)


class CoffeeMachine(CoffeeGrinder, FrenchPress):
	americano_drink = 0  # Переменная для подсчёта напитков американо

	def make_americano_drink(self, count):  # Метод для приготовления американо
		coffee_drink_requirement = 1  # Количество необходимого молотого кофе для американо
		water_drink_requirement = 2  # Количество необходимого воды для американо
		if cm.coffee == 0 or cm.water == 0:
			print(f'В машине отсутствует молотый кофе, или вода')
		else:
			coffee_drink_requirement *= count
			water_drink_requirement *= count
			if coffee_drink_requirement > self.coffee or water_drink_requirement > cm.water:
				print(f'Невозможно сделать {count} американо из-за нехватки ингридиентов в автомате.\n'
					  f'Требуется {coffee_drink_requirement} молотого кофе или {water_drink_requirement} воды')
			else:
				self.americano_drink += count
				print('Сделано американо', self.americano_drink)
				cm.coffee -= coffee_drink_requirement
				cm.water -= water_drink_requirement

	def get_coffee_drink(self, count):  # Метод, используемый для выдачи напитков американо из автомата
		if self.americano_drink == 0:
			print('Кофе нет')
		elif count > self.americano_drink:
			print('Невозможно выдать американо больше, чем есть в автомате:', self.americano_drink)
		else:
			print('Выдано американо', count)
			self.americano_drink -= count

	def count_americano_drink(self):  # Метод для получения информации о количество напитков кофе, имеющегося в автомате
		print("Количество американо хранящегося в автомате: ", self.americano_drink)


cm = CoffeeMachine()
cm.put_beans(10)  # Кладём в гриндер 10 бобов
cm.grind()  # Вызываем метод гринд, в результате работы которого, мы получим 10 молотого кофе
cm.put_water(50)  # Кладём в автомат 50 единиц воды
cm.put_coffee(20)  # Кладём в автомат ещё 20 молотого кофе (с учётом тех  10 = 30)
cm.count_coffee_drink()  # Проверяем наличие напитков кофе в автомате: их 0
cm.make_coffee_drink(10)  # Готовим 10 напитков кофе
cm.count_coffee_drink()  # Проверяем наличие напитков кофе в автомате: их 10
cm.count_americano_drink()  # Проверяем наличие напитков американо в автомате: их 0
cm.make_americano_drink(20)  # Готовим 20 напитков американо
cm.count_americano_drink()  # Проверяем наличие напитков американо в автомате: их 20
# После этого, в автомате не осталось ингридиентов для приготовления любого из напитков, для проверки попробуем приготовить ещё по одной порции напитка
cm.make_coffee_drink(1)  # Выдаст ошибку об отсутствии ингридиентов
cm.make_americano_drink(1)  # Выдаст ошибку об отсутствии ингридиентов
