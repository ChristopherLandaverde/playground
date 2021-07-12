<template>
<div class="page-client">
    <div class='columns is-multiline'>
        <div class="column is-12">
            <h1 class="title">Details</h1>
                  <router-link :to="{ name: 'EditCubed'}" class="button is-info mt-4"> Edit Idea</router-link>
                <button class="button is-danger mt-4" @click ="deleteIdea">Delete Idea </button>
            </div>
        


            <div class="column is-12">


                <p><strong>Analyzed Idea: </strong> {{idea.analyzed_idea}}</p>
            
                <p v-if="idea.applyed_idea"><strong>Applyed Idea: </strong> {{idea.applyed_idea}} </p>
             
          
                <p v-if="idea.argued_idea "><strong>Described Idea: </strong>{{idea.argued_idea}} </p>
              
                <p v-if="idea.associate_idea "><strong>Different Idea: </strong>{{idea.associate_idea}} </p>
                 
                <p v-if="idea.compared_idea "><strong>Compared Idea: </strong>{{idea.compared_idea}} </p>
                 
                <p v-if="idea.described_idea "><strong>Described Idea: </strong>{{idea.described_idea}} </p>
 
        

                </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'




export default {
    name:'CubedIdeas',
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
            .get(`api/v1/cubing/${ideaID}`)
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
            .delete(`api/v1/cubing/${ideaID}`)
            .then(response => {
                console.log(response)
                this.idea = response.data
            })
            this.$router.push(`/cubing`)
            .catch(error=> {
                console.log(JSON.stringify(error))
            })

        },
    }
}
</script>
