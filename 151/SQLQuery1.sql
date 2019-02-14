CREATE DATABASE types_db;
GO

USE types_db;
GO

CREATE TABLE types_tbl(

id int,
[name] nvarchar(4)

);


CREATE TABLE alltypes_tbl(

[bit] bit,
[tinyint] tinyint,
[smallint] smallint,
[bigint] bigint,
[decimal] decimal,
[money] money,
[float] float,
[date] date,
[datetime] datetime,
[time] time,
[datetime2] datetime2,
[datetimeoffset] datetimeoffset,
[char] char,
[varchar] varchar,
[nchar] nchar,
[nvarchar] nvarchar,
[binary] binary,
[varbinary] varbinary,
[uniqueidentifier] uniqueidentifier,
[sql_variant] sql_variant,
[xml] xml,
[geometry] geometry,
[geography] geography

);


