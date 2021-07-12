<template>
    <div class="page-add-client">
        <div class="column is-12">
            <h1 class="title">Edit Idea </h1>
            </div>
            
            <div class="column is-12">
                <div class="container">
  <h1 class="title">Analyzed Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.analyzed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
     <div class="container">
  <h1 class="title">Applyed Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.analyzed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
     <div class="container">
  <h1 class="title">Argued Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.argued_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<div class="container">
  <h1 class="title">Associate Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.associate_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>

  <div class="container">
  <h1 class="title">Compared Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.compared_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>

    <div class="container">
  <h1 class="title">Described Idea </h1>
  <h2 class="subtitle">
   What is the goal you are trying to achieve? </h2>
    <div class="control">
        <textarea  v-model="cubed_idea.described_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
 </div>


            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click ="submitIdea">Save Changes</button>
                     
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
            cubed_idea:{}

        }
    },
    async mounted() {
        await this.getBrainIdea()
    },
    methods: {
            getBrainIdea() {
            const ideaID= this.$route.params.id

            axios 
            .get(`api/v1/cubing/${ideaID}`)
            .then(response => {
                console.log(response)
                this.cubed_idea = response.data
            })
            .catch(error=> {
                console.log(JSON.stringify(error))
            })

        },
        submitIdea() {
            const ideaID= this.$route.params.id

            axios
            .patch(`/api/v1/cubing/${ideaID}/`,this.cubed_idea)
            .then(response => {

                    toast({
                    message:'The Client was Edited',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:2000,
                    position: 'bottom-right',
                })
                this.$router.push(`/cubing/${ideaID}`)
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
        },


    }
}
</script>
