<template lang="pug">
+each("students as student")
  p {student.name}
  p {student.age}
  p ----------
</template>

<script>
import axios from "axios"
import { onMount } from "svelte"

let baseAPI = "http://0.0.0.0:8000/api"
let rest = true
let students = []

onMount(async () => {
  let params = {}
  const res = await axios({
    method: "get",
    url: baseAPI
  })
  console.log(res.data)
  students = res.data
})

</script>

<style>
p {
  color: blue;
}
</style>
