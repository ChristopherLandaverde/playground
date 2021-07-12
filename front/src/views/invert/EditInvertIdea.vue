<template>
    <div class="page-add-client">
        <div class="column is-12">

<div class="container">
  <h1 class="title">Idea</h1>
  <h2 class="subtitle">
    A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading. </h2>
    <div class="control">
        <textarea  v-model="editInvertedIdea.idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
</div>
<br>
  <div class="container">
  <h1 class="title">Reversed Idea</h1>
  <h2 class="subtitle">
    A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading. </h2>
    <div class="control">
        <textarea  v-model="editInvertedIdea.reversed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
 <div class="container">
  <h1 class="title">Decisions</h1>
  <h2 class="subtitle">
    A simple container to divide your page into <strong>sections</strong>, like the one you're currently reading. </h2>
    <div class="control">
        <textarea  v-model="editInvertedIdea.wrong" class="textarea" placeholder="Textarea"></textarea>
        </div>
 </div>

 <br>
 <div class="field is-grouped">
  <div class="control">
    <button class="button is-link" @click ="submitIdea">Save Changes </button>
  </div>
  <div class="control">
    <button class="button is-link is-light">Cancel</button>
  </div>
 
 </div>
 
</div>

</div>


   
     
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'


export default {
    name: 'EditInvertIdea',
    data(){
        return {
            editInvertedIdea:{}

        }
    },
    async mounted() {
        await this.getBrainIdea()
    },
    methods: {
            getBrainIdea() {
            const ideaID= this.$route.params.id

            axios 
            .get(`api/v1/inverts/${ideaID}`)
            .then(response => {
                console.log(response)
                this.editInvertedIdea = response.data
            })
            .catch(error=> {
                console.log(JSON.stringify(error))
            })

        },
        submitIdea() {
            const ideaID= this.$route.params.id

            axios
            .patch(`/api/v1/inverts/${ideaID}/`,this.editInvertedIdea)
            .then(response => {

                    toast({
                    message:'The Client was Edited',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:2000,
                    position: 'bottom-right',
                })
                this.$router.push(`/invert/${ideaID}`)
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        },


    }
}
</script>
