class Boggle_Game{
    constructor(board){
        this.board = $(`#${board}`);
        //console.log("hello")

        $(".guess_form", this.board).on("submit", this.handleSubmit.bind(this))
    }

    

    showWord(word){
        $("#entered_words", this.board).append($("<li>", {text: word}));
    }

    async handleSubmit(e){
        e.preventDefault() //preventing refresh

        const $guess = $('#guess_input', this.board);

        let word = $guess.val();

        console.log(word);

        this.showWord(word);
        //check server for word value
        //const response = await axios.get("/guess");

        //console.log(response);


    }

}

//
new Boggle_Game()