import java.util.Scanner;


public class Player {
    private final int id;
    private final String name;
    private final char marker;
    private final Scanner sc;
    private int numberOfWins;

    public Player(String name, int id, char marker) {
        this.id = id;
        this.name = name;
        this.numberOfWins = 0;
        this.marker = marker;
        sc = new Scanner(System.in);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return this.name;
    }

    public char getMarker() {
        return this.marker;
    }

    public Scanner getSC() {
        return this.sc;
    }

    public void closeSC() {
        this.sc.close();
    }

    public int getNumberOfWins() {
        return this.numberOfWins;
    }

    public void incrementNumberOfWins() {
        this.numberOfWins++;
    }

    public void resetNumberOfWins() {
        this.numberOfWins = 0;
    }

    public void move(Board board) {
        String movePos;

        while (true) {
            System.out.println("Player " + this.name + ", please enter your move. (enter a value from 1 - " + board.getBoardSize() * board.getBoardSize() + ")");
            board.print();

            if (sc.hasNextLine()) {
                movePos = sc.nextLine();

                if (!board.isValidPosition(movePos)) {
                    System.out.println("Invalid move. Please try again.");
                } else {
                    break;
                }
            }
        }

        board.placeTheMove(this.marker, Integer.parseInt(movePos));
    }
}
