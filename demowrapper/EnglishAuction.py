class EnglishAuction:
	"""
	An Auction Library
	Timed auction starting at a low price and increasing until no more bids are made.
	Also supports reserve price and automatic bidding.
	"""

	def Create(start: int, end: int, startingPrice: int, reservePrice: int) -> bool:
		"""		Create a new auction
		Args:
			start (int):start time of auction
			end (int):end time of auction
			startingPrice (int):starting price of auction
			reservePrice (int):reserve price for the auction (0 = none)
		Returns:
			RET HERE
		"""
	def Bid(auctionId: int, userId: int, price: int) -> bool:
		"""		Bid in an auction
		Args:
			auctionId (int):auction id to bid in
			userId (int):user id that's bidding
			price (int):bid price
		Returns:
			RET HERE
		"""
	def AutoBid(auctionId: int, userId: int, price: int) -> bool:
		"""		Automatically bid against others in an auction (up to the specified amount)
		Args:
			auctionId (int):auction id to bid in
			userId (int):user id that's bidding
			price (int):bid price
		Returns:
			RET HERE
		"""
	def ForceClose(auctionId: int, userId: int, price: int) -> bool:
		"""		Force an auction to close and specify the winning bid.
		Args:
			auctionId (int):auction id to bid in
			userId (int):user id that's bidding
			price (int):bid price
		Returns:
			RET HERE
		"""
	def Status():
		"""		TBD
		Args:
		"""
#END
