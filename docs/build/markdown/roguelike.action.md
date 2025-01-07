# roguelike.action package

## Submodules

## roguelike.action.action_entity module

### *class* roguelike.action.action_entity.Action(type: int)

Базовые классы: `object`

Action logic.

#### *abstract* run() → None

Run logic.

### *class* roguelike.action.action_entity.ItemAction(type: int, id: int, user_controller: [UserController](roguelike.md#roguelike.user_controller.UserController))

Базовые классы: [`Action`](#roguelike.action.action_entity.Action)

ItemAction logic.

#### run() → None

Run logic.

### *class* roguelike.action.action_entity.MovingAction(type: int, entity: [AbstractObject](roguelike.entities.md#roguelike.entities.abstract_object.AbstractObject), user_controller: [UserController](roguelike.md#roguelike.user_controller.UserController))

Базовые классы: [`Action`](#roguelike.action.action_entity.Action)

MovingAction logic.

#### run() → None

Run logic.

### *class* roguelike.action.action_entity.SpellAction(type: int, map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap), user: [User](roguelike.entities.md#roguelike.entities.user.User), move_size: int)

Базовые классы: [`Action`](#roguelike.action.action_entity.Action)

ItemAction logic.

#### run() → None

Run logic.

## Module contents
