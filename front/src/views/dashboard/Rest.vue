<template>
  <div class="column is-12">
    <div class="field">
        <h1> <strong>FreeWriting</strong> </h1>
        
        <div class="control">
        <textarea  v-model="rest.freewrite" class="textarea" placeholder="Textarea"></textarea>
        </div>
    <div class="field">
     <label> Any Links that you wanted to add?</label>
     <input class="input is-primary" v-model="rest.links" type="text" placeholder="Primary input">
    </div>
    </div>

<div class="field is-grouped">
  <div class="control">
    <button class="button is-link" @click ="submitForm">Submit</button>
  </div>
  <div class="control">
    <button class="button is-link is-light">Cancel</button>
  </div>
 
 </div>
 </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'Rest',
    data(){
        return {
            rest:{}
        }
    },
    methods: {
        submitForm (){
                axios
                .post('api/v1/rests/',this.rest)
                .then(response =>{
                    console.log(response)    
                })
                 this.$router.push('/dashboard/ideas')
        }
        
    }
}
</script>
