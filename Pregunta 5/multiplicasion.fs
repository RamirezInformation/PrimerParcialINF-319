// Your code here!
open System

let multi a b = 
    let lista = [for i in 1..b -> a]
    let suma = List.sum lista
    printfn "La multiplicacion de %dx%d es:  %d" 10 15 suma
    


[<EntryPoint>]
let main argv =
    multi 10 15
    Console.ReadKey() |>ignore
    0 // return an integer exit code