open System

let numeros = [|9;8;7;6;15;14;12;22;21;29|]
printfn "-------Lista Original-------:"
printfn("%A") numeros
printfn" "

let pares = [for i in numeros do if i%2=0 then yield i]
let impares = [for i in numeros do if i%2=1 then yield i]

printfn "-------Lista números pares-------"
printfn("%A") pares
printfn" "

printfn "-------Lista números impares-------"
printfn("%A") impares