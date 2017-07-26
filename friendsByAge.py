from mrjob.job import MRJob

class FriendsByAge(MRJob):
	def mapper(self,key,line):
		(ID,Name,Age,NumberofFriends)=line.split(',')
		yield Age,float(NumberofFriends)

	def reducer(self,Age,NumberofFriends):
		total=counter=0
		for number in NumberofFriends:
			total+=number
			counter+=1
		average=total/counter
		yield Age,average

if __name__=='__main__':
	FriendsByAge.run()