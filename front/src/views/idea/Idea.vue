<template>
<div class="page-client">
    <div class='columns is-multiline'>
        <div class="column is-12">
            <h1 class="title">Idea Details</h1>
                  <router-link :to="{ name: 'EditBrainIdea'}" class="button is-info mt-4"> Edit Idea</router-link>
           
                 <button class="button is-danger mt-4" @click ="deleteIdea">Delete Idea </button>
            </div>
        


            <div class="column is-12">

             
                <p><strong>Goals: </strong> {{idea.goals}}</p>
                
                  <p v-if="idea.agenda"><strong>Agenda:</strong> {{idea.agenda}} </p>

                <p v-if="idea.decisions"><strong>Decisions:</strong> {{idea.decisions}} </p>
      
                <p v-if="idea.outcomes "><strong>Outcomes:</strong>{{idea.outcomes}} </p>
 
        

                </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'



export default {
    name:'Idea',
    data(){
        return {
            idea: {},
       
     
        }
    },
   async  mounted() {
        await this.getIdea()
     
      
    },
    methods: {
        getIdea() {
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

        deleteIdea() {
             const ideaID= this.$route.params.id

            axios
            .delete(`/api/v1/brainstorms/${ideaID}/`,this.brainidea)
            .then(response => {

                    toast({
                    message:'The Client was Deleted',
                    type: 'is-dangerous',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:4000,
                    position: 'bottom-right',
                })
                this.$router.push('/ideas')
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        }
    }
}
</script>
