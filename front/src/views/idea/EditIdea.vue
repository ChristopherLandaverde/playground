<template>
    <div class="page-add-client">
        <div class="column is-12">


  <div class="container">
  <h1 class="title">Goals </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="idea.goals" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
<div class="container">
  <h1 class="title">Agenda</h1>
  <h2 class="subtitle">
    List of items that will be solved with this goal.</h2>
    <div class="control">
        <textarea  v-model="idea.agenda" class="textarea" placeholder="Textarea"></textarea>
        </div>
</div>
<br>
  <div class="container">
  <h1 class="title">Outcomes</h1>
  <h2 class="subtitle">
    What outcome would you like to come from this goal? </h2>
    <div class="control">
        <textarea  v-model="idea.outcomes" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
 <div class="container">
  <h1 class="title">Decisions</h1>
  <h2 class="subtitle">
    Any thoughts to conclude from this? </h2>
    <div class="control">
        <textarea  v-model="idea.decisions" class="textarea" placeholder="Textarea"></textarea>
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
    name: 'EditBrainIdea',
    data(){
        return {
            idea:{}

        }
    },
    async mounted() {
        await this.getBrainIdea()
    },
    methods: {
            getBrainIdea() {
            const ideaID= this.$route.params.id

            axios 
            .get(`api/v1/brainstorms/${ideaID}`)
            .then(response => {
                console.log(response)
                this.idea = response.data
            })
            .catch(error=> {
                console.log(JSON.stringify(error))
            })

        },
        submitIdea() {
            const ideaID= this.$route.params.id

            axios
            .patch(`/api/v1/brainstorms/${ideaID}/`,this.idea)
            .then(response => {

                    toast({
                    message:'The Client was Edited',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:2000,
                    position: 'bottom-right',
                })
                this.$router.push(`/ideas/${ideaID}`)
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        },


    }
}
</script>
