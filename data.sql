Declare @Id int
Set @Id = 1

While @Id <= 1000000
Begin 
   Insert Into products values ('shape - ' + CAST(@Id as nvarchar(10)),
              'size - ' + CAST(@Id as nvarchar(10)) + ' name')
              'location - ' + CAST(@Id as nvarchar(10)) + ' name')
              'price - ' + CAST(@Id as nvarchar(10)) + ' name')
   Print @Id
   Set @Id = @Id + 1
End