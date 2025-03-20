import matplotlib.pyplot as plt
import io
import base64

class Calc:
    """
    Класс для расчета сложных процентов с учетом ежемесячных пополнений.
    """

    def __init__(self, start, rate, years, monthly_deposit=0):
        """
        Инициализация калькулятора.
        """
        self.start = start
        self.rate = rate / 100
        self.years = years
        self.monthly_deposit = monthly_deposit

    def calc(self):
        """
        Рассчитывает сложные проценты с учетом ежемесячных пополнений.
        """
        monthly_rate = self.rate / 12
        months = self.years * 12
        total = self.start
        history = [self.start]

        for _ in range(months):
            total = (total + self.monthly_deposit) * (1 + monthly_rate)
            history.append(total)

        profit = total - self.start - (self.monthly_deposit * months)
        return round(total, 2), round(profit, 2), history

    def generate_plot(self, history):
        """
        Генерирует график роста суммы.
        """
        plt.figure(figsize=(8, 6))
        plt.plot(history)
        plt.xlabel('Месяцы')
        plt.ylabel('Сумма')
        plt.title('Рост суммы с учетом сложных процентов')
        plt.grid(True)

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()

        return plot_url