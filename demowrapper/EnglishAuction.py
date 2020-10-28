class EnglishAuction:
	"""
	An Auction Library
	Timed auction starting at a low price and increasing until no more bids are made.
	Also supports reserve price and automatic bidding.
	"""

	def Create(start: int, end: int, startingPrice: int, reservePrice: int, priceIncrement: int) -> bool:
		"""		Create a new auction
		Args:
			start (int):start time of auction
			end (int):end time of auction
			startingPrice (int):starting price of auction
			reservePrice (int):reserve price for the auction (0 = none)
			priceIncrement (int):price increments for bids in the auction
		Returns:
			RET HERE
		"""
	def GetStart(auctionId: int) -> bool:
		"""		Get the start of an auction
		Will return a timestamp in milliseconds
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetEnd(auctionId: int) -> bool:
		"""		Check if auction has ended
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def HasStarted(auctionId: int) -> bool:
		"""		Check if an auction has started yet
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def Bid(auctionId: int, userId: int, price: int):
		"""		Create a bid in an auction
		Args:
			auctionId (int):auction id
			userId (int):user id
			price (int):price bud
		"""
	def GetHighestBidder(auctionId: int) -> bool:
		"""		Get the highest bidder in an auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetHighestBids(auctionId: int, numBids: int) -> bool:
		"""		Get the highest bids in an auction
		Args:
			auctionId (int):auction id
			numBids (int):max number of highest bids to return
		Returns:
			RET HERE
		"""
	def GetNumberOfBids(auctionId: int) -> bool:
		"""		Get the number of bids in an auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetPriceIncrement(auctionId: int) -> bool:
		"""		Get the price increment for the specified auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetReservePrice(auctionId: int) -> bool:
		"""		Get the reserve price for the specified auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetStartingPrice(auctionId: int) -> bool:
		"""		Get the starting price for the specified auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def CalcTimeRemaining(auctionId: int, now: int) -> bool:
		"""		Get the time remaining for the specified auction
		Args:
			auctionId (int):auction id
			now (int):current unix timestamp
		Returns:
			RET HERE
		"""
	def CalcMinimumBid(auctionId: int) -> bool:
		"""		Get the minimum next bid for the specified auction
		Args:
			auctionId (int):auction id
		Returns:
			RET HERE
		"""
	def GetAuctionsEnding(endfrom: int, endto: int, page: int, perpage: int, sort: int, asc: int) -> bool:
		"""		Get a list of auctions based on their end time
		Args:
			endfrom (int):end from
			endto (int):end to
			page (int):
			perpage (int):number of auctions per page
			sort (int):field to sort by
			asc (int):ascending (true) or descending (false)
		Returns:
			RET HERE
		"""
	def GetAuctionsStarting(startfrom: int, startto: int, page: int, perpage: int, sort: int, asc: int) -> bool:
		"""		Get a list of auctions based on their start time
		Args:
			startfrom (int):start from
			startto (int):start to
			page (int):
			perpage (int):number of auctions per page
			sort (int):field to sort by
			asc (int):ascending (true) or descending (false)
		Returns:
			RET HERE
		"""
	def GetOpenAuctions(page: int, perpage: int, sort: int, asc: int) -> bool:
		"""		Get a list of currently running auctions
		Args:
			page (int):
			perpage (int):number of auctions per page
			sort (int):field to sort by
			asc (int):ascending (true) or descending (false)
		Returns:
			RET HERE
		"""
#END
