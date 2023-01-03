from FulltimeEmployee import FulltimeEmployee
from HourlyEmployee import HourlyEmployee
from Payroll import Payroll

payroll = Payroll()

payroll.add(FulltimeEmployee('Barry', 'Goodall', 6000))
payroll.add(FulltimeEmployee('Rob', 'Jesson', 6500))
payroll.add(HourlyEmployee('Rahima', 'Habib', 200, 50))
payroll.add(HourlyEmployee('Vanessa', 'Green', 150, 100))
payroll.add(HourlyEmployee('Nicola', 'Harrison', 100, 150))

payroll.print()
