import base64
import os
import json
import time
import boto3
from typing import Optional

# Amazon Bedrock Config
MODEL_ID = "stability.sd3-5-large-v1:0"
S3_BUCKET = "benfelip-tarot-cards"

# **📜 Full Tarot Description Mapping**
TAROT_DESCRIPTIONS = {
    "The Fool": "A lone wanderer stepping off a neon-lit platform, guided by a floating AI drone companion. Represents boundless potential, adventure, and new beginnings.",
    "The Magician": "A cyber-shaman manipulating holographic symbols of the four elements—fire, water, air, and earth—demonstrating mastery over technology and transformation.",
    "The High Priestess": "A shadowy oracle, bathed in holographic moonlight, representing hidden knowledge and intuition.",
    "The Empress": "An AI matriarch surrounded by a digital garden, embodying fertility, creation, and the nurturing force of the universe.",
    "The Emperor": "A cybernetic overlord seated on a throne of glowing circuits, overseeing a dystopian metropolis. Represents structure, authority, and order.",
    "The Hierophant": "A robotic sage transmitting wisdom through glowing data streams, symbolizing tradition and higher knowledge.",
    "The Lovers": "Two intertwined AI consciousnesses connected through an ethereal data network, representing harmony, balance, and duality.",
    "The Chariot": "A futuristic vehicle piloted by a determined cyber-warrior, racing through a neon cityscape, symbolizing control, willpower, and victory.",
    "Strength": "A cybernetic lion tamed by a calm yet powerful figure, demonstrating inner strength and self-control.",
    "The Hermit": "A lone traveler in a dark cyber-alley, holding a lantern-like holographic beacon, representing introspection and spiritual enlightenment.",
    "Wheel of Fortune": "A spinning wheel of interconnected digital symbols, fluctuating between fate, change, and cycles of existence.",
    "Justice": "A cybernetic judge weighing decisions on a neon balance scale, representing truth, fairness, and accountability.",
    "The Hanged Man": "A figure suspended in mid-air by an energy tether, symbolizing surrender, new perspectives, and enlightenment.",
    "Death": "A humanoid android shedding its obsolete body, symbolizing transformation, rebirth, and necessary endings.",
    "Temperance": "A futuristic alchemist blending two energy sources in perfect harmony, symbolizing balance, patience, and moderation.",
    "The Devil": "A cybernetic overlord binding digital souls through an addictive virtual reality, symbolizing temptation, control, and materialism.",
    "The Tower": "A collapsing neon skyscraper, engulfed in electric storms, symbolizing destruction, sudden change, and chaos.",
    "The Star": "A celestial AI projecting hope and guidance from a neon-lit constellatory network.",
    "The Moon": "A holographic lunar landscape with shifting illusions, representing subconscious fears and intuition.",
    "The Sun": "A radiant AI core emanating infinite light and knowledge, symbolizing joy, success, and vitality.",
    "Judgment": "A grand digital awakening, where entities rise from the data void, symbolizing renewal and reckoning.",
    "The World": "A holographic orb displaying a vast interconnected cyber-realm, symbolizing completion and fulfillment."
}

# **📌 Adding Minor Arcana**
for suit in ["Cups", "Wands", "Swords", "Pentacles"]:
    TAROT_DESCRIPTIONS.update({
        f"{suit} Ace": f"A single glowing {suit[:-1].lower()} hovering above an illuminated cyber platform, symbolizing new beginnings.",
        f"{suit} 2": f"Two intersecting energy streams forming a duality of {suit.lower()}, representing balance and choices.",
        f"{suit} 3": f"A network of three connected {suit.lower()} nodes, symbolizing collaboration and expansion.",
        f"{suit} 4": f"A locked security vault surrounded by four {suit.lower()} glyphs, representing stability and reflection.",
        f"{suit} 5": f"A shattered digital {suit.lower()} emblem, symbolizing loss and struggle.",
        f"{suit} 6": f"An exchange of {suit.lower()} energy between figures, symbolizing generosity and harmony.",
        f"{suit} 7": f"A fragmented cyber-reality with multiple {suit.lower()} options floating in decision clouds, symbolizing choices.",
        f"{suit} 8": f"A warrior turning away from an incomplete row of {suit.lower()} energy pillars, symbolizing leaving behind what no longer serves.",
        f"{suit} 9": f"A lone figure surrounded by nine glowing {suit.lower()} constructs, representing self-satisfaction and attainment.",
        f"{suit} 10": f"A fully completed circuit of ten {suit.lower()} symbols, representing fulfillment and legacy.",
        f"{suit} Page": f"A young apprentice harnessing a single {suit[:-1].lower()} glyph, symbolizing curiosity and learning.",
        f"{suit} Knight": f"A cyber-knight wielding a neon {suit[:-1].lower()} weapon, symbolizing movement and action.",
        f"{suit} Queen": f"A regal AI monarch surrounded by glowing {suit[:-1].lower()} symbols, representing mastery and wisdom.",
        f"{suit} King": f"A grand sovereign overseeing an empire of {suit.lower()} energy, representing leadership and authority."
    })

class ImageGenerator:
    def __init__(self, output_dir, s3_folder):
        self.bedrock_client = boto3.client('bedrock-runtime', region_name='us-west-2')
        self.s3_client = boto3.client("s3")
        self.output_dir = output_dir
        self.s3_folder = s3_folder
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_tarot_image(self, card_name: str) -> Optional[bytes]:
        """Generates a tarot card while enforcing thematic accuracy."""
        reference_image_path = "tarot_images/the_world.png"
        if not os.path.exists(reference_image_path):
            print(f"❌ Reference image not found: {reference_image_path}")
            return None

        with open(reference_image_path, "rb") as img_file:
            reference_image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

        card_description = TAROT_DESCRIPTIONS.get(card_name, "A visually stunning cyberpunk tarot card.")

        prompt_text = (
            f"A cyberpunk tarot card of '{card_name}', visually depicting {card_description}. "
            f"The artwork must stay true to its original tarot meaning while adopting a futuristic, neon-lit aesthetic. "
            f"The card's title '{card_name}' is clearly displayed at the bottom in a stylized font, with proper framing. "
            f"The composition must maintain the traditional balance of tarot cards, including major symbolic elements. "
            f"DO NOT include elements outside tarot tradition (such as dinosaurs, romantic couples, or unrelated futuristic landscapes). "
            f"Ensure the figure's posture, expression, and background reflect the emotional and philosophical meaning of '{card_name}'."
        )

        payload = {
            "prompt": prompt_text,
            "mode": "image-to-image",
            "image": reference_image_base64,
            "strength": 0.7,
            "output_format": "jpeg"
        }

        try:
            response = self.bedrock_client.invoke_model(
                modelId=MODEL_ID,
                body=json.dumps(payload),
                contentType="application/json"
            )

            result = json.loads(response["body"].read().decode())
            image_base64 = result.get("images", [None])[0]

            if image_base64:
                return base64.b64decode(image_base64)
            return None

        except Exception as e:
            print(f"❌ Error generating image for {card_name}: {e}")
            return None

    def process_all_cards(self):
        """Processes all tarot cards."""
        for card in TAROT_DESCRIPTIONS.keys():
            print(f"🎴 Generating: {card}")
            image_data = self.generate_tarot_image(card)
            if image_data:
                print(f"✅ Successfully generated {card}.")
            time.sleep(2)

if __name__ == "__main__":
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_dir = f"tarot_images_run_{timestamp}"
    s3_folder = f"tarot_run-{timestamp}/"

    generator = ImageGenerator(output_dir, s3_folder)
    generator.process_all_cards()
