from mrjob.job import MRJob 
from mrjob.step import MRStep
import re

class spendByCustomer(MRJob):

	def steps(self):
		return [
			MRStep(mapper=self.mapper_get_data,
					reducer=self.reducer_get_sum),
			MRStep(mapper=self.mapper_make_sum_key,
					reducer=self.reducer_output_result)
		]

	def mapper_get_data(self,_,line):
		(user,item,amount)=line.split(",")
		yield user,float(amount)

	def reducer_get_sum(self,user,amount):
		
		yield user,sum(amount)

	def mapper_make_sum_key(self,users,amount):
		yield amount,users

	def reducer_output_result(self,amount,users):
		for user in users:
			yield user,amount

if __name__ == '__main__':
	spendByCustomer.run()


