def nbMonths(old_car_price, new_car_price, saving_per_month, percent_loss_by_month):
    available = old_car_price - new_car_price

    months = 1
    while available < 0:
        percent = percent_loss_by_month / 100
        old_car_price = old_car_price - old_car_price * percent
        new_car_price = new_car_price - new_car_price * percent
        available = old_car_price + saving_per_month * months - new_car_price

        months += 1
        if months % 2 == 0:
            percent_loss_by_month += 0.5

    return [months - 1, round(available)]
