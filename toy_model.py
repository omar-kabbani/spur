# Set up a toy model

from spur.core import Model
from spur.core.route import Route
from spur.core.component.trackway import SingleBlockTrack

# Instantiate a model
model = Model()
components = []
components.append(
    model.add_component(SingleBlockTrack, "1", "2", "A", length=80, track_speed=25)
)
components.append(
    model.add_component(SingleBlockTrack, "2", "3", "A", length=30, track_speed=15)
)
components.append(
    model.add_component(SingleBlockTrack, "3", "4", "A", length=450, track_speed=25)
)
components.append(
    model.add_component(SingleBlockTrack, "4", "5", "A", length=1050, track_speed=25)
)
components.append(
    model.add_component(SingleBlockTrack, "5", "6", "A", length=650, track_speed=25)
)
route = Route()
for c in components:
    route.append(c)

route.segments[2].departure = 90
# Plop a train onto the component
train = model.add_train("CX1", "1", "2", "A", max_speed=20, route=route)
train = model.add_train("CX2", "1", "2", "A", max_speed=19, route=route)
model.start()
model.run(until=500)
