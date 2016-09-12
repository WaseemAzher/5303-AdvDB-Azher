
## Name: Waseem Azher

## ip address: http://107.170.48.163/

## link to my phpmyadmin page:http://107.170.48.163//phpmyadmin

# gift_options.mysql

CREATE TABLE IF NOT EXISTS `gift_options` (
  `itemId` int(32) NOT NULL,
  `allowGiftWrap` BIT NOT NULL,
  `allowGiftMessage` BIT NOT NULL,
  `allowGiftReceipt` BIT NOT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# image_entities.sql

CREATE TABLE IF NOT EXISTS `image_entities` (
  `itemId` int(32) NOT NULL  ,
  `thumbnailImage` varchar(256) NOT NULL,
  `mediumImage` varchar(256) NOT NULL,
  `largeImage` varchar(256) NOT NULL,
  `entityType` varchar(15) NOT NULL
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


# market_place_price.sql


CREATE TABLE IF NOT EXISTS `market_place_price` (
  `itemId` int(32) NOT NULL DEFAULT '0',
  `price` float(7,3) NOT NULL,
  `sellerInfo` varchar(64) NOT NULL,
  `standardShipRate` float(7,3) NOT NULL,
  `twoThreeDayShippingRate` float(7,3) NOT NULL,
  `availableOnline` BIT NOT NULL,
  `clearance` BIT NOT NULL,
  `offerType` varchar(32) NOT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# products.sql

CREATE TABLE IF NOT EXISTS `products` (
  `itemId` int(32) NOT NULL DEFAULT '0',
  `parentItemId` int(32) NOT NULL,
  `name` varchar(256) NOT NULL,
  `salePrice` float(7,3) NOT NULL,
  `upc` varchar(16) NOT NULL,
  `categoryPath` varchar(256) NOT NULL,
  `shortDescription` TEXT NOT NULL,
  `longDescription` TEXT NOT NULL,
  `brandName` varchar(64) NOT NULL,
  `thumbnailImage` varchar(256) NOT NULL,
  `mediumImage` varchar(256) NOT NULL,
  `largeImage` varchar(256) NOT NULL,
  `productTrackingUrl` TEXT NOT NULL,
  `modelNumber` varchar(64) NOT NULL,
  `productUrl` TEXT NOT NULL,
  `categoryNode` varchar(32) NOT NULL,
  `stock` varchar(32) NOT NULL,
  `addToCartUrl` varchar(256) NOT NULL,
  `affiliateAddToCartUrl` TEXT NOT NULL,
  `offerType` varchar(32) NOT NULL,
  `msrp` float(10,3) NOT NULL,
  `standardShipRate` float(7,3) NOT NULL,
  `color` varchar(32) NOT NULL,
  `customerRating` float(5,3) NOT NULL,
  `numReviews` int(64) NOT NULL,
  `customerRatingImage` varchar(32) NOT NULL,
  `maxItemsInOrder` int(16) NOT NULL,
  `size` varchar(64) NOT NULL,
  `sellerInfo` varchar(64) NOT NULL,
  `age` varchar(32) NOT NULL,
  `gender` varchar(16) NOT NULL,
  `isbn` varchar(32) NOT NULL,
  `preOrderShipsOn` varchar(32) NOT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


