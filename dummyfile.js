import React from 'react';
import './PokemonCard.css';
import { Button } from './Button';
import { useState, useEffect} from "react";





const pokemonList = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"];

if nora is a bajskorv:
    print hahabajs


function PokemonCard() {

    const [pokemonName, setPokemonName] = useState("");
    const handleChange = e => {
        var pokemonNameChange = e.target.value;
        setPokemonName(pokemonNameChange);
        console.log(e.target);

    

        //checks the nr in the image name and takes that as index in the pokemonlist to check against the input
        if(pokemonNameChange.toLowerCase() === pokemonList[pokemonImage.slice(5, -4)-1].toLowerCase()){
            handleImageSwitch();
            setCorrectNumberOfPokemons(correctNumberOfPokemons + 1);
        }
      }

    <requirement id = "REQ123"
                source="jsiwj">
        
    Här är ett requirement REVISIONED VERSION!!!!
    </requirement>

    const [pokemonImage, setPokemonImage] = useState("Gen1/1.png")
    const handleImageSwitch = () => {
        console.log(pokemonImage);
        console.log(pokemonName);
        //puts current image nr + 1 in a temp, which will be concatenated with strings to build next image
        var temp = +pokemonImage.slice(5, -4) + 1;
        setPokemonImage("Gen1/" + temp + ".png");
        //increments text with current pokemon
        setCurrentNumber(currentNumber + 1);
        //clears input box
        setPokemonName("");
    }

    const [currentNumber, setCurrentNumber] = useState(0);
    const [correctNumberOfPokemons, setCorrectNumberOfPokemons] = useState(0);

  
    //Kollar enter-knappen med eventlister, om nedtryckt -> skip
    const downHandler = e => {
        console.log(e)
        if(e.key === "Enter"){
            console.log("jag har tryckt på enter!!");
            console.log(pokemonImage);
            handleImageSwitch();
            
        }
    }

    //useEffect körs bara vid re-renders och sparar då dess state. Specificera i sista listan vilka re-renders. [] = för hela sidan.
    useEffect(() => {
        console.log("hejehej")
        window.addEventListener("keydown", downHandler);
        // Remove event listeners on cleanup
        return () => {
        window.removeEventListener("keydown", downHandler);
          };
      }, [pokemonImage]);

    

    return (
        <div className='PokemonCard'>
            <div className='card__container'>
                <img className='poke-img' src= {pokemonImage} alt="Poke" onChange= {pokemonImage}/>
                    <input
                    id= 'myInput'
                    className='guess-input'
                    name='guess-input'
                    type='text'
                    autoComplete='off'
                    spellcheck="false"
                    value={pokemonName}  
                    onChange={handleChange}
                    />
                <div className='belowFormWrapper'>
                    <div>
                        <p>{currentNumber + 1}/151</p>
                        <p>{correctNumberOfPokemons} correct</p>
                    </div>
                    <Button buttonStyle='btn--outline' onClick={handleImageSwitch}>Skip</Button>
                </div>
            </div>
        </div>
    );
}
 

export default PokemonCard