export default defineEventHandler(async (event) => {
    const postBody = await readBody(event)
    const job = postBody.job
    console.log(job)
    const resp = await $fetch("http://127.0.0.1:8000/generate", { body: { "job_description": job }, method: "POST" })

    return resp
    
})