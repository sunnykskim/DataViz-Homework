Sub Easy()

'loop through all sheets
For Each ws In Worksheets
ws.Activate

'variable assignment
Dim summaryrow As Integer
Dim totalstockvolume As Double
Dim ticker As String

'output column headers
Range("i1").Value = "Ticker"
Range("j1").Value = "Total Stock Volume"

'last row
lastrow = ws.Cells(Rows.Count, 1).End(xlUp).row

'give variables starting value
totalstockvolume = 0
summaryrow = 2

'for loop!!

For i = 2 To lastrow
    'check if we are still within same ticker, if it is...
    If Range("A" & i + 1).Value = Range("A" & i).Value Then
        'add to totalstockvolume
        totalstockvolume = totalstockvolume + Range("G" & i).Value
    'if it is no longer the same...
    Else
        'set the ticker name
        ticker = Range("A" & i).Value
        'print ticker in summary column
        Range("I" & summaryrow).Value = ticker
        'print totalstockvolume in summary column
        Range("j" & summaryrow).Value = totalstockvolume + Range("g" & i).Value
        'add one to summary row to start new ticker
        summaryrow = summaryrow + 1
        'reset totalstockvolume total
        totalstockvolume = 0
        
        End If
        

Next i

Next ws
    
End Sub

