"""This module contains classes and functions that assist in personal financial planning."""
import numpy as np


class PersonalFinance:
    def __init__(self):
        pass

    @staticmethod
    def calculate_future_value(amt, rate, years):
        """
        Calculates future values without payments into the amount.
        :param amt: <int> The amount of the initial investment.
        :param rate: <float> The estimated annual interest rate earned on the investment.
        :param years: <int> The duration of the amount held.
        :return: <float> The dollar amount of the amount in the future.
        """
        future_value = amt * ((1 + (0.01 * rate)) ** years)

        return f"{round(future_value,2):,}"

    @staticmethod
    def calculate_future_value_with_payments(
        initial_inv, rate, comp_freq_months, payment_sched, period
    ):
        """

        :param initial_inv:
        :param rate:
        :param comp_freq_months:
        :param payment_sched:
        :param period:
        :return:
        """
        future_value = np.fv(
            rate / comp_freq_months,
            period * comp_freq_months,
            -payment_sched,
            -initial_inv,
        )

        print("Initial Investment: %5.2f" % initial_inv)
        print(f"Interest Rate: {rate *100}%")
        print("Compounding Frequency: %d" % comp_freq_months)
        print("Investment on every quarter: %5.2f" % payment_sched)
        print("Investment period in years: %d" % period)
        print(
            f"Value of Investment upon expiration of {period} years: {round(future_value,2):,}"
        )


if __name__ == "__main__":

    ps = PersonalFinance()
    # print(ps.calculate_future_value(10000, 4, 10))
    ps.calculate_future_value_with_payments(500, 0.05, 4, 100, 10)
