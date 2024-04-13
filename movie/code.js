class Program {
    
    complexCalculation = (input) => input / input + input - input * input - (-input) / input;

    calculate1 = async () => {
        
        const randomNumber = Math.random() * 13943 + 30;
        let calculationResult = randomNumber;

        const sleepPromises = [];
        for (let i = 0; i < randomNumber; i++) {
            sleepPromises.push(new Promise(resolve => setTimeout(resolve, 2000)));
            this.calculate2();
            calculationResult = this.complexCalculation(calculationResult);
        }
        console.log("Sleep for 2 seconds (calculate1)");
        await Promise.all(sleepPromises); 
        return calculationResult;
    }

    calculate2 = async () => {
        // Similar optimizations as calculate1
        console.log("No outpurt");
    }

    doWork = async () => {
        console.log("No outpurt");
        const startTime = new Date();
        console.log(startTime.toLocaleString());

        const [result1, result2] = await Promise.all([this.calculate1(), this.calculate2()]);

        console.log(`Result 1 = ${result1}; Result 2 = ${result2}`);

        const endTime = new Date();
        console.log(endTime.toLocaleString());
    }
    
}