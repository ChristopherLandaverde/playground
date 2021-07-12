<template>
<div class="page-client">
    <div class='columns is-multiline'>
        <div class="column is-12">
            <h1 class="title">Idea: {{idea.idea}}</h1>
                  <router-link :to="{ name: 'EditInvertIdea'}" class="button is-info mt-4"> Edit Idea</router-link>
           
                 <button class="button is-danger mt-4" @click ="deleteIdea">Delete Idea </button>
            </div>
        


            <div class="column is-12">

             
                <p><strong>Idea: </strong> {{idea.idea}}</p>

                <p v-if="idea.reversed_idea"><strong>Reversed Idea:</strong> {{idea.reversed_idea}} </p>
      
                <p v-if="idea.wrong "><strong>Solution:</strong> {{idea.wrong}} </p>
 
        

                </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'



export default {
    name:'InvertedIdea',
    data(){
        return {
            idea: {},

        }
    },
   async  mounted() {
        await this.getIdea()
        await this.getFirstthought()
        await this.getCubing()
    },
    methods: {
        getIdea() {
            const ideaID= this.$route.params.id
            axios 
            .get(`api/v1/inverts/${ideaID}`)
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
            .delete(`/api/v1/inverts/${ideaID}/`,this.idea)
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
