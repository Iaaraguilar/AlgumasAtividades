idade = int(input("Digite sua idade: "))
match idade:
    case idade if idade < 16:
        print("Proibido votar.")
    case idade if 16 <= idade < 18:
        print("Voto optativo.")
    case idade if 18 <= idade < 65:
        print("Voto obrigatório.")
    case idade if idade >= 65:
        print("Voto optativo.")
