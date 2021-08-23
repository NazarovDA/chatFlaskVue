<template>
    <div>
        <div class="textbox">
            <ol>
                <li v-for="message in messages" :key="message.id">
                    {{new Date(message.time).toLocaleString()}} {{message.author}} {{message.text}} {{message.isSent}} {{message.id}}
                </li>
            </ol>
        </div>
        <div class="current_message">
            <input v-model="message" type="text" placeholder="input your text here" autocomplete="false" v-on:keypress.enter="send_message">
            <button v-on:click.prevent="send_message">Send message</button>
        </div>
        <div>
            <button v-on:click.prevent="update">Update messages</button>
        </div>
    </div>
</template>

<script>
export default {
    name:"chat",
    data(){
        return {
            name: "",
            messages: [
                
            ],
            message: ""
        }
    },
    methods: {
        async send_message(){
            const url = "localhost:5000"
            let data = {
                time: Date.now(),
                author: this.name,
                text: this.message,
                isSent: false
            };
            this.messages.push(data);
            data = this.messages[this.messages.length-1];
            const Response = await fetch(
                `//${url}/get_message`,
                {
                    method: "POST",
                    headers:{
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    body: JSON.stringify(data)
                }
            )
            let res = await Response.json()
            if (Response.status === 200 && res["time"] === data.time){
                data.isSent = true;
                data.id = res["id"]
            }
            this.message = "";
            this.update();
        },
        async update(){
            const url = "localhost:5000"
            console.log(this)
            let Response = await fetch(
                `//${url}/get_message?from_id=${this.messages.length > 0 ? this.messages[this.messages.length-1].id: 0}`,
                {
                    method:"GET",
                }
            )
            let res = await Response.json()

            if (Response.status === 200){
                this.messages.push(...res)
            }
        }
    },
    mounted(){
        this.update()
        this.name = localStorage.getItem("username")
        setInterval(this.update, 5000)
    }   
}
</script>

<style>

</style>