const addWine = () => {
    event.preventDefault()
    const newField = document.createElement('div')
    newField.innerHTML = `
        <div>
            <label for="wines">Wine Pairing</label>
            <input name="wines" id="wines" />
            <button onclick="addWine()">+</button>
            <button onclick="removeItem()">-</button><br />
        </div>`
    document.querySelector('#wines-container').appendChild(newField)
}

const addAllergen = () => {
    event.preventDefault()
    const newField = document.createElement('div')
    newField.innerHTML = `
        <div>
            <label for="allergens">Allergen</label>
            <input name="allergens" id="allergens" />
            <button onclick="addAllergen()">+</button>
            <button onclick="removeItem()">-</button><br />
        </div>`
    document.querySelector('#allergens-container').appendChild(newField)
}

const removeItem = () => {
    event.preventDefault()
    event.target.parentElement.remove()
}